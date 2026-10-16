
"""Manage a radio station's programme schedule safely."""

import ast
import operator
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    """
    CREATE TABLE slots (
        id INTEGER PRIMARY KEY,
        show TEXT,
        host TEXT,
        start_hour INTEGER,
        minutes INTEGER
    )
    """
)

_BINARY_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
}

_COMPARISON_OPERATORS = {
    ast.Lt: operator.lt,
    ast.LtE: operator.le,
    ast.Gt: operator.gt,
    ast.GtE: operator.ge,
    ast.Eq: operator.eq,
    ast.NotEq: operator.ne,
}


def add_slot(show, host, start_hour, minutes):
    """Add a radio programme to the schedule."""
    conn.execute(
        """
        INSERT INTO slots (show, host, start_hour, minutes)
        VALUES (?, ?, ?, ?)
        """,
        (show, host, start_hour, minutes),
    )


def slot_label(show, host):
    """Return a readable label for a radio programme."""
    return f"{show} hosted by {host}"


def _evaluate_node(node):
    """Evaluate only supported arithmetic and comparison expressions."""
    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        return node.value

    if isinstance(node, ast.BinOp):
        operation = _BINARY_OPERATORS.get(type(node.op))
        if operation is None:
            raise ValueError("Unsupported arithmetic operator")

        left = _evaluate_node(node.left)
        right = _evaluate_node(node.right)
        return operation(left, right)

    if isinstance(node, ast.UnaryOp):
        if isinstance(node.op, ast.UAdd):
            return _evaluate_node(node.operand)
        if isinstance(node.op, ast.USub):
            return -_evaluate_node(node.operand)
        raise ValueError("Unsupported unary operator")

    if isinstance(node, ast.Compare):
        left = _evaluate_node(node.left)

        for operation_node, comparator in zip(
            node.ops, node.comparators
        ):
            operation = _COMPARISON_OPERATORS.get(type(operation_node))
            if operation is None:
                raise ValueError("Unsupported comparison operator")

            right = _evaluate_node(comparator)
            if not operation(left, right):
                return False
            left = right

        return True

    raise ValueError("Unsupported expression")


def overlap_free(formula):
    """Safely evaluate a simple arithmetic or comparison formula."""
    try:
        expression = ast.parse(formula, mode="eval")
        return _evaluate_node(expression.body)
    except (
        SyntaxError,
        ValueError,
        TypeError,
        ZeroDivisionError,
        OverflowError,
    ):
        return False


def morning_shows():
    """Return programme names starting before noon when slots exist."""
    total_minutes = conn.execute(
        "SELECT COALESCE(SUM(minutes), 0) FROM slots"
    ).fetchone()[0]

    if total_minutes > 0:
        rows = conn.execute(
            "SELECT show FROM slots WHERE start_hour < ?",
            (12,),
        )
        return [row[0] for row in rows]

    return []


def remove_slot(slot_id):
    """Remove a programme using its slot ID."""
    conn.execute("DELETE FROM slots WHERE id = ?", (slot_id,))


def main():
    """Demonstrate the radio schedule operations."""
    add_slot("Sunrise Beats", "Vik", 7, 60)
    add_slot("Midday Talk", "Anu", 13, 45)
    print(slot_label("Sunrise Beats", "Vik"))
    print(overlap_free("7 + 1 <= 13"), morning_shows())
    remove_slot(2)


if __name__ == "__main__":
    main()

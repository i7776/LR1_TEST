
def print_table_header():
    """ONLY prints table header"""
    print("\n" + "="*70)
    print(f"| {'x':^10} | {'n':^6} | {'F(x)':^15} | {'Math F(x)':^15} | {'eps':^10} |")
    print("="*70)

def print_table_row(x, n, f_x, math_f_x, eps):
    """ONLY prints one table row"""
    print(f"| {x:^10.4f} | {n:^6} | {f_x:^15.10f} | {math_f_x:^15.10f} | {eps:^10.2e} |")

def print_table_footer():
    """ONLY prints table footer"""
    print("="*70)

import os
import circle
import square

def main():
    shape = os.environ.get("SHAPE", "circle").lower()
    value = float(os.environ.get("VALUE", "1"))

    if shape == "circle":
        print("shape=circle")
        print("r=", value)
        print("area=", circle.area(value))
        print("perimeter=", circle.perimeter(value))

    elif shape == "square":
        print("shape=square")
        print("a=", value)
        print("area=", square.area(value))
        print("perimeter=", square.perimeter(value))

    else:
        raise ValueError("SHAPE must be 'circle' or 'square'")

if __name__ == "__main__":
    main()

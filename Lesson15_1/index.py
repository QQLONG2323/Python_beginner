from tools import add
from tools import Tool
from tools import ONE, TWO, THREE, FOUR, FIVE

def main() -> None:
    print(add(4.2, 9.5))
    print(Tool.add(3.2, 9.5))
    print(ONE, TWO, THREE, FOUR, FIVE)
    print(Tool.ONE, Tool.TWO, Tool.THREE, Tool.FOUR, Tool.FIVE)
    Tool.a()

if __name__ == "__main__":
    main()
import random
from datetime import datetime
from pathlib import Path

class LuckyNumberGenerator:

    def __init__(self, output_dir: str = "output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate_number(self) -> int:
        return random.randint(1, 100)

    def save_number(self, lucky_number: int) -> bool:
        output_file = self.output_dir / "lucky_number.txt"
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"🍀 Your lucky number for {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {lucky_number}\n")
            print(f"Lucky number saved to {output_file}")
            return True
        except IOError as e:
            print(f"Error saving lucky number to file: {e}")
            return False

def main():
    generator = LuckyNumberGenerator()
    lucky_number = generator.generate_number()
    generator.save_number(lucky_number)

if __name__ == '__main__':
    main()

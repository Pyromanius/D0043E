import re


def count_word_frequency(text: str) -> dict:
	if not isinstance(text, str):
		raise TypeError("text must be a string")

	words = re.findall(r"\w+", text.lower())

	freq = {}
	for w in words:
		freq[w] = freq.get(w, 0) + 1
	return freq


def bubble_sort(word_list: list) -> list:
	arr = word_list[:]
	n = len(arr)

	for i in range(n):
		swapped = False
		for j in range(0, n - i - 1):
			a = arr[j].get('count', 0)
			b = arr[j + 1].get('count', 0)
			if a < b:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				swapped = True
		if not swapped:
			break
	return arr


def _to_list_of_dicts(freq_dict: dict) -> list:
	return [{'word': w, 'count': c} for w, c in freq_dict.items()]


def main():
	text = input("Enter a sentence: ").strip()
	if not text:
		print("No text entered. Exiting.")
		return

	freq = count_word_frequency(text)
	word_list = _to_list_of_dicts(freq)
	sorted_list = bubble_sort(word_list)

	while True:
		n_input = input("How many top words to show (N)? ").strip()
		try:
			n = int(n_input)
			if n <= 0:
				print("Please enter a positive integer.")
				continue
			break
		except ValueError:
			print("Invalid number. Please enter an integer.")

	top_n = sorted_list[:n]
	print(f"\nTop {len(top_n)} words:")
	for i, item in enumerate(top_n, start=1):
		print(f"{i}. {item['word']}: {item['count']}")


if __name__ == '__main__':
	main()

def max_boxes(input_file="input2.txt", output_file="output2.txt"):
    try:
        with open(input_file, "r") as f_in:
            n = int(f_in.readline().strip())
            boxes = []
            for _ in range(n):
                line = f_in.readline().strip()
                w, c = map(int, line.split())
                boxes.append((w, c))

    except FileNotFoundError:
        print(f"Ошибка: Файл {input_file} не найден.")
        return
    except ValueError:
        print(f"Ошибка: Некорректный формат входных данных в файле {input_file}.")
        return
    except Exception as e:
        print(f"Ошибка: Произошла ошибка при чтении файла: {e}")
        return

    boxes.sort(key=lambda x: x[0] + x[1])

    count = 0
    all_weights = 0

    for weight, capacity in boxes:
        if all_weights <= capacity:
            all_weights += weight
            count += 1

    try:
        with open(output_file, "w") as f_out:
            f_out.write(str(count) + "\n")

    except Exception as e:
        print(f"Ошибка: Произошла ошибка при записи в файл: {e}")
        return


if __name__ == "__main__":
    max_boxes()

def schedule_lectures(input_file="input1.txt", output_file="output1.txt"):
    try:
        with open(input_file, "r") as f_in:
            n = int(f_in.readline().strip())
            requests = []
            for _ in range(n):
                line = f_in.readline().strip()
                s, f = map(int, line.split())
                requests.append((s, f))

    except FileNotFoundError:
        print(f"Ошибка: Файл {input_file} не найден.")
        return
    except ValueError:
        print(f"Ошибка: Некорректный формат входных данных в файле {input_file}.")
        return
    except Exception as e:
        print(f"Ошибка: Произошла ошибка при чтении файла: {e}")
        return

    requests.sort(key=lambda x: x[1])

    schedule = []
    last_end_time = 0

    for start_time, end_time in requests:
        if start_time >= last_end_time:
            schedule.append((start_time, end_time))
            last_end_time = end_time

    schedule.sort(key=lambda x: x[0])

    try:
        with open(output_file, "w") as f_out:
            for start_time, end_time in schedule:
                f_out.write(f"{start_time} {end_time}\n")

    except Exception as e:
        print(f"Ошибка: Произошла ошибка при записи в файл: {e}")
        return


if __name__ == "__main__":
    schedule_lectures()

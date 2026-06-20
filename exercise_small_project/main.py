import file_utils
import analyser

def main():
    calls = file_utils.load_json_file("calls.json")

    if calls == None:
        return

    analysis = analyser.analyse_calls(calls)

    file_utils.save_json_file("analysis.json", analysis)

    print(analysis)

if __name__ == "__main__":
    main()
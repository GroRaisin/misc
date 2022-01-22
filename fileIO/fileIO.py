
def main():
    with open("test_file", "r") as fin:
        with open("out_file", "w") as fout:
            for line in fin:
                print(repr(line))
                out_line = line.replace("include", "exclude")
                fout.write(out_line)



if __name__ == '__main__':
    main()
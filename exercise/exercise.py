# Add my first name in the beginning of every line and my last name in the end of every line
f_name = input(">>> Enter file name to modify")
f = open(f_name, "r")
lines = f.readlines()
final_list = map(lambda s: "Tomer " + str(s).strip("\n") + " Rosenfeld\n", lines)
f.close()
final_file = open("final_" + f_name, "w")
final_file.writelines(final_list)
final_file.close()

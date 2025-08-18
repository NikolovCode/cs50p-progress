def main():
    name = input("Enter file name: ")
    name_new = name.lower().strip()
    extensions(name_new)

def extensions(s):
     suffix = s.split('.')[-1]
     match suffix:
          case "jpeg":
            print("image/jpeg")
          case "jpg":
            print("image/jpeg")
          case "gif":
            print("image/gif")
          case "pdf":
            print("application/pdf")
          case "zip":
            print("application/zip")
          case "png":
            print("image/png")
          case "txt":
            print("text/plain")
          case _:
            print("application/octet-stream")

main()

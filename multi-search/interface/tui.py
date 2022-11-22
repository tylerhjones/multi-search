
def print_verison():
  from importlib.metadata import version, PackageNotFoundError

  try:
      __version__ = version("package-name")
  except PackageNotFoundError:
      # package is not installed
      pass

def main():
    print("Hello multi!")


if __name__ == "__main__":
    main()
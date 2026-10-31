#This line is for running the app
def greet(name):
    return f"Hello, {name}! Welcome to GitHub Actions."


def add(a, b):
    return a + b


if __name__ == "__main__":
    print(greet("DevOps Engineer"))
    print("Addition result:", add(10, 20))

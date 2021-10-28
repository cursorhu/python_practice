developer = {
    'alice': ['python', 'ruby'],
    'bruce': ['golang', 'python'],
    'cindy': ['C++', 'shell', 'rust'],
}

for name, languages in developer.items():
    print(name + "'s skilled languages are:")
    for lang in languages:
        print(lang)



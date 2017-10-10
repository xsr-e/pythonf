def cached_default(a = []):
    a.append('*')
    return ''.join(a)

print(cached_default())
print(cached_default())
print(cached_default())
print(cached_default())
print(cached_default())
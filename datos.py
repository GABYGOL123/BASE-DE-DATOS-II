from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Functions to generate data
def generate_solo_internet():
    return {
        "Nombre": fake.name(),
        "Direccion": fake.address().replace('\n', ' '),
        "Tipo de Servicio": "Internet",
        "Velocidad de Internet (Mbps)": f"{random.randint(10, 100)}",
        "Email": fake.email()
    }

def generate_internet_fijo():
    return {
        "Nombre": fake.name(),
        "Direccion": fake.address().replace('\n', ' '),
        "Tipo de Servicio": "Internet + Fijo",
        "Velocidad de Internet (Mbps)": f"{random.randint(10, 100)}",
        "Telefono Fijo": fake.phone_number(),
        "Email": fake.email()
    }

def generate_internet_fijo_tv():
    return {
        "Nombre": fake.name(),
        "Direccion": fake.address().replace('\n', ' '),
        "Tipo de Servicio": "Internet + Fijo + TV",
        "Velocidad de Internet (Mbps)": f"{random.randint(10, 100)}",
        "Telefono Fijo": fake.phone_number(),
        "Canales de TV": random.randint(50, 200),
        "Email": fake.email()
    }

# Generate data
solo_internet = [generate_solo_internet() for _ in range(5000)]
internet_fijo = [generate_internet_fijo() for _ in range(5000)]
internet_fijo_tv = [generate_internet_fijo_tv() for _ in range(5000)]

# Convert data to string format with double spaces between columns
def format_data(data):
    headers = data[0].keys()
    rows = ['  '.join(headers)]
    for entry in data:
        rows.append('  '.join(str(entry.get(header, '')).ljust(30) for header in headers))
    return '\n'.join(rows)

# Get formatted data
solo_internet_data = format_data(solo_internet)
internet_fijo_data = format_data(internet_fijo)
internet_fijo_tv_data = format_data(internet_fijo_tv)

# Define file paths
path_solo_internet = r'C:\Users\valdi\Desktop\BD2\solo_internet.txt'
path_internet_fijo = r'C:\Users\valdi\Desktop\BD2\internet_fijo.txt'
path_internet_fijo_tv = r'C:\Users\valdi\Desktop\BD2\internet_fijo_tv.txt'

# Save to files
with open(path_solo_internet, 'w') as f:
    f.write(solo_internet_data)

with open(path_internet_fijo, 'w') as f:
    f.write(internet_fijo_data)

with open(path_internet_fijo_tv, 'w') as f:
    f.write(internet_fijo_tv_data)

print("Archivos generados exitosamente en C:\\Users\\valdi\\Desktop\\BD2")

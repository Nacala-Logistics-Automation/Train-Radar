import pandas as pd
from fastkml import kml
from shapely.geometry import LineString

def parse_kml(kml_file):
    with open(kml_file, 'rb') as file:
        doc = file.read()

    k = kml.KML()
    k.from_string(doc)

    features = list(k.features())
    if not features:
        print("Nenhum recurso encontrado no KML.")
        return []

    document = features[0]
    print(f"Documento KML lido com sucesso: {document.name}")

    placemarks = []
    for feature in document.features():
        if isinstance(feature, kml.Folder):
            print(f"Processando pasta: {feature.name}")
            for placemark in feature.features():
                extract_coordinates(placemark, placemarks)
        elif isinstance(feature, kml.Placemark):
            print(f"Processando placemark: {feature.name}")
            extract_coordinates(feature, placemarks)

    if not placemarks:
        print("Nenhum placemark encontrado no KML.")
    return placemarks

def extract_coordinates(placemark, placemarks):
    if placemark.geometry:
        geom_type = placemark.geometry.geom_type
        if geom_type == 'LineString':
            coords_list = list(placemark.geometry.coords)
            for coords in coords_list:
                placemarks.append([placemark.name, coords[0], coords[1]])
                print(f"LineString coordenada: {placemark.name}, {coords[0]}, {coords[1]}")
        else:
            print(f"Geometria não suportada: {geom_type}")
    else:
        print(f"Placemark sem geometria: {placemark.name}")

kml_file = r'C:\Users\vdx7607\Desktop\Amostra Banco ACT\NACALA CORRIDOR - COAL.kml'
data = parse_kml(kml_file)

if data:
    # Cria um DataFrame a partir dos dados extraídos
    df = pd.DataFrame(data, columns=['Nome', 'Longitude', 'Latitude'])

    # Salva o DataFrame em um arquivo Excel
    output_file = 'saida.xlsx'
    df.to_excel(output_file, index=False)

    print(f'Arquivo Excel salvo em: {output_file}')
else:
    print("Nenhum dado encontrado para salvar no Excel.")

import folium
import pandas as pd
import requests

blc = pd.read_json('https://www.bicilascondes.cl/availability_map/getJsonObject')  # BiciLasCondes

js = requests.get('https://api.citybik.es/v2/networks/santiago').json()  # BikeSantiago
bs = pd.DataFrame(js['network']['stations']).rename(columns={'latitude': 'lat', 'longitude': 'lon'})


def get_mobike(lat, lon):
    url = 'https://mwx.mobike.com/mobike-api/rent/nearbyBikesInfo.do'
    post_fields = {'header': 'bar', 'latitude': lat, 'longitude': lon}
    json = requests.post(url, post_fields).json()
    mb = pd.DataFrame(json['object']).rename(columns={'distY': 'lat', 'distX': 'lon'})
    return mb


bases = blc.sample(10)[['lat', 'lon']].values
mb = pd.concat(get_mobike(*base) for base in bases)

blc['sistema'] = 'bicilascondes';
bs['sistema'] = 'bikesantiago';
mb['sistema'] = 'mobike'
merged = blc.append(bs).append(mb)
print('%d stations total' % len(merged))

centroide = list(merged[['lat', 'lon']].median())
# centroide
merged['color'] = merged.sistema.apply(lambda s: 'red' if s == 'mobike'
else 'green' if s == 'bicilascondes' else 'orange')
fm = folium.Map(location=centroide, width=1000, height=600, zoom_start=12, tiles='CartoDBdark_matter')
for sistema, sisdata in merged.groupby('sistema'):
    for id, row in sisdata.iterrows():
        folium.Circle((row['lat'], row['lon']), color=row['color']).add_to(fm)

fm
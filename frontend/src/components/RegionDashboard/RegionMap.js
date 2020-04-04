import React from "react";
import { Map, TileLayer, GeoJSON, Marker, Popup } from "react-leaflet";
import "./RegionMap.css";
import data from "../../assets/json/perifereies-rescaled.json";

export function RegionMap({ regionId }) {
	const center = [38.664896, 23.318018];
	const zoom = 7;
	console.log(data);
	const centers = data.features.forEach(feature => {
		console.log(feature.geometry);
	});
	// ((feature) => {
	// 	return feature.geometry.getBounds().getCenter();
	// });

	function showName(feature, layer) {
		if (feature.properties && feature.properties.PER) {
			layer.bindPopup(feature.properties.PER);
		}
	}

	return (
		<Map className="region-map" center={center} zoom={zoom}>
			<TileLayer
				attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
				url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
			/>
			<GeoJSON
				data={data}
				color="black"
				fillColor="blue"
				onEachFeature={showName}
				pointToLayer={function(geoJsonPoint, latlng) {
					return <Marker position={latlng}>

					</Marker>}}
			/>
			{/* {centers.map((center) => {
				return (
					<Marker position={center}>
						<Popup>
							{center}
						</Popup>
					</Marker>
				);
			})} */}
		</Map>
	);
}

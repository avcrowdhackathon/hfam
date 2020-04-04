import React from "react";
import { Map, TileLayer } from "react-leaflet";
import "./HospitalsMap.css";
import { HospitalMarker } from "../HospitalMarker/HospitalMarker";

export function HospitalsMap(props) {
	const center = [38.664896, 23.318018];
	const zoom = 7;
	const sampleHospital = {
		name: "test",
		capacity: 400,
		occupancy: 180,
		facilities: [
			"Ογκολογικό",
			"Ακτινολογικό",
			"Μονάδα έκτακτης διαχείρισης"
		],
		coords: [38.664896, 23.318018],
		id: 15
	};

	return (
		<Map className="hospitals-map" center={center} zoom={zoom}>
			<TileLayer
				attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
				url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
			/>
			<HospitalMarker hospital={sampleHospital} />
		</Map>
	);
}

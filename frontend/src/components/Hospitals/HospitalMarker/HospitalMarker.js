import React from "react";
import { Marker, Popup } from "react-leaflet";
import {HospitalDetails} from "../HospitalDetails/HospitalDetails";

export function HospitalMarker({ hospital }) {
    const {coords, id, ...details } = hospital;
	return (
		<Marker position={coords}>
			<Popup>
                <HospitalDetails details={details} />
			</Popup>
		</Marker>
	);
}

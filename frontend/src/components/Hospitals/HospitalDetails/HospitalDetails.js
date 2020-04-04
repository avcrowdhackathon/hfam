import React from "react";

export function HospitalDetails({ details : { name, capacity, occupancy, facilities } }) {
	const available = capacity - occupancy;
	return (
		<article>
			<h3>{name}</h3>
			<dl>
				<dt>Διαθέσιμες κλίνες</dt>
				<dd>{available}</dd>
				<dt>Σύνολο κλινών</dt>
				<dd>{capacity}</dd>
				<dt>Διαθέσιμες Υποδομές</dt>
				<dd>
					<ul>
						{facilities.map(facility => (
							<li>{facility}</li>
						))}
					</ul>
				</dd>
			</dl>
		</article>
	);
}

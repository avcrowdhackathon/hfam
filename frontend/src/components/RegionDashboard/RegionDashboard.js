import React, { useState, useEffect } from "react";
import { RegionMap } from "./RegionMap";
import { Col, Row } from "reactstrap";

export function RegionDashboard(props) {
	const [regions, setRegions] = useState([]);

	useEffect(() => {
		fetch("http://hfam.team/api/regions/")
			.then(res => res.json())
			.then(json => console.log(json))
			.catch(err => console.log(err));
	}, [])

	return (
		<div className="content">
			<Row>
				<Col md="12">
					<RegionMap>
                        
                    </RegionMap>
				</Col>
			</Row>
		</div>
	);
}

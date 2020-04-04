import React from "react";
import { Col, Card, CardBody, CardTitle, Row } from "reactstrap";

export function InfoCard({icon, description, info, footer}) {
	return (
		<Col lg="4" md="6">
			<Card className="card-stats">
				<CardBody>
					<Row>
						<Col xs="5">
							<div className="info-icon text-center icon-warning">
								<i className={icon} />
							</div>
						</Col>
						<Col xs="7">
							<div className="numbers">
								<p className="card-category">{description}</p>
								<CardTitle tag="h3">{info}</CardTitle>
							</div>
						</Col>
					</Row>
				</CardBody>
				{footer}
			</Card>
		</Col>
	);
}

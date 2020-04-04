import React, {useState} from "react";
import {
	Row,
	Col,
	CardFooter,
	Card,
	CardHeader,
	CardTitle,
	ButtonGroup,
	Button,
	CardBody
} from "reactstrap";
import { InfoCard } from "components/InfoCard/InfoCard";
import { HospitalsMap } from "../HospitalsMap/HospitalsMap";
import classNames from "classnames";
import { Line } from "react-chartjs-2";

// core components
import {
    chartExample1,
    } from "../../../variables/charts";

export function HospitalDashboard(props) {
    const [currentData, setData] = useState("data1");

	return (
		<div className="content">
			<Row>
				<InfoCard
					icon="fas fa-head-side-cough"
					description="Επιβαιβεωμένα"
					info="1200"
					footer={
						<CardFooter>
							<hr />
							<div className="stats">
								<i className="tim-icons icon-refresh-01" />{" "}
								Update Now
							</div>
						</CardFooter>
					}
				/>
				<InfoCard
					icon="fas fa-bed"
					description="Διασωληνωμένοι"
					info="90"
					footer={
						<CardFooter>
							<hr />
							<div className="stats">
								<i className="tim-icons icon-refresh-01" />{" "}
								Update Now
							</div>
						</CardFooter>
					}
				/>
				<InfoCard
					icon="fas fa-first-aid"
					description="Θεραπευμένοι"
					info="350"
					footer={
						<CardFooter>
							<hr />
							<div className="stats">
								<i className="tim-icons icon-refresh-01" />{" "}
								Update Now
							</div>
						</CardFooter>
					}
				/>
			</Row>
			<Row>
				<Col md="8">
					<HospitalsMap></HospitalsMap>
				</Col>
				<Col md="4">
					<Card className="card-chart">
						<CardHeader>
							<Row>
								<Col className="text-left" sm="6">
									<h5 className="card-category">
										Total Shipments
									</h5>
									<CardTitle tag="h2">Performance</CardTitle>
								</Col>
								<Col sm="6">
									<ButtonGroup vertical
										className="btn-group-toggle float-right"
										data-toggle="buttons"
									>
										<Button
											color="info"
											id="0"
											size="sm"
											tag="label"
											className={classNames(
												"btn-simple",
												{
													active:
														currentData ===
														"data1"
												}
                                            )}
                                            style={{
                                                marginLeft: 0
                                            }}
											onClick={() =>
												setData(data => "data1")
											}
										>
											<input
												defaultChecked
												name="options"
												type="radio"
											/>
											<span className="d-none d-sm-block d-md-block d-lg-block d-xl-block">
												Accounts
											</span>
											<span className="d-block d-sm-none">
												<i className="tim-icons icon-single-02" />
											</span>
										</Button>
										<Button
											color="info"
											id="1"
											size="sm"
											tag="label"
											className={classNames(
												"btn-simple",
												{
													active:
														currentData ===
														"data2"
												}
											)}
											onClick={() =>
												setData(data => "data2")
											}
										>
											<input
												name="options"
												type="radio"
											/>
											<span className="d-none d-sm-block d-md-block d-lg-block d-xl-block">
												Purchases
											</span>
											<span className="d-block d-sm-none">
												<i className="tim-icons icon-gift-2" />
											</span>
										</Button>
										<Button
											color="info"
											id="2"
											size="sm"
											tag="label"
											className={classNames(
												"btn-simple",
												{
													active:
														currentData ===
														"data3"
												}
											)}
											onClick={() =>
												setData(data => "data3")
											}
										>
											<input
												name="options"
												type="radio"
											/>
											<span className="d-none d-sm-block d-md-block d-lg-block d-xl-block">
												Sessions
											</span>
											<span className="d-block d-sm-none">
												<i className="tim-icons icon-tap-02" />
											</span>
										</Button>
									</ButtonGroup>
								</Col>
							</Row>
						</CardHeader>
						<CardBody>
							<div className="chart-area">
								<Line
									data={
										chartExample1[currentData]
									}
									options={chartExample1.options}
								/>
							</div>
						</CardBody>
					</Card>
				</Col>
			</Row>
		</div>
	);
}

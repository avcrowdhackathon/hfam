import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import "./assets/css/bootstrap.min.css";
import "./assets/css/black-dashboard-pro-react.min.css";
import "react-notification-alert/dist/animate.css";
import "@fortawesome/fontawesome-free/css/all.css";
import { App } from "./App";

ReactDOM.render(
	<React.StrictMode>
		<App />
	</React.StrictMode>,
	document.getElementById("root")
);
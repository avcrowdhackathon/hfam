
import React from "react";
import { createBrowserHistory } from "history";
import { Router, Route, Switch, Redirect } from "react-router-dom";

import { DefaultLayout } from "./layouts/DefaultLayout";

import "./assets/css/nucleo-icons.css";

import "./App.css";

const hist = createBrowserHistory();

export function App() {

	return (
		<Router history={hist}>
			<Switch>
				<Route
					path="/admin"
					render={props => <DefaultLayout {...props} />}
				/>
				<Redirect from="/" to="/admin/dashboard" />
			</Switch>
		</Router>
	);
}

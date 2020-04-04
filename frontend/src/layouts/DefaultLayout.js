import React from "react";
import { Route, Switch, Redirect } from "react-router-dom";
// react plugin for creating notifications over the dashboard
import NotificationAlert from "react-notification-alert";

// core components
import { DefaultNavbar } from "../components/Navbars/DefaultNavbar";
import { Footer } from "../components/Footer/Footer";
import Sidebar from "../components/Sidebar/Sidebar";

import routes from "../routes";

import logo from "./../assets/img/react-logo.png";

const activeColor = "blue";

export class DefaultLayout extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			sidebarMini: true,
			opacity: 0,
			sidebarOpened: false
		};
		this.mainPanel = React.createRef();
		this.notificationAlert = React.createRef();
	}
	showNavbarButton = () => {
		if (
			document.documentElement.scrollTop > 50 ||
			document.scrollingElement.scrollTop > 50 ||
			this.refs.mainPanel.scrollTop > 50
		) {
			this.setState({ opacity: 1 });
		} else if (
			document.documentElement.scrollTop <= 50 ||
			document.scrollingElement.scrollTop <= 50 ||
			this.refs.mainPanel.scrollTop <= 50
		) {
			this.setState({ opacity: 0 });
		}
	};
	getRoutes = routes => {
		return routes.map((prop, key) => {
			if (prop.collapse) {
				return this.getRoutes(prop.views);
			}
			if (prop.layout === "/admin") {
				return (
					<Route
						path={prop.layout + prop.path}
						component={prop.component}
						key={key}
					/>
				);
			} else {
				return null;
			}
		});
	};
	getActiveRoute = routes => {
		let activeRoute = "Default Brand Text";
		for (let i = 0; i < routes.length; i++) {
			if (routes[i].collapse) {
				let collapseActiveRoute = this.getActiveRoute(routes[i].views);
				if (collapseActiveRoute !== activeRoute) {
					return collapseActiveRoute;
				}
			} else {
				if (
					window.location.pathname.indexOf(
						routes[i].layout + routes[i].path
					) !== -1
				) {
					return routes[i].name;
				}
			}
		}
		return activeRoute;
	};
	toggleSidebar = () => {
		this.setState({
			sidebarOpened: !this.state.sidebarOpened
		});
		document.documentElement.classList.toggle("nav-open");
	};
	closeSidebar = () => {
		this.setState({
			sidebarOpened: false
		});
		document.documentElement.classList.remove("nav-open");
	};

	render() {
		return (
			<div className="wrapper">
				<div className="rna-container">
					<NotificationAlert ref={this.notificationAlert} />
				</div>
				<div
					className="navbar-minimize-fixed"
					style={{ opacity: this.state.opacity }}
				>
					<button
						className="minimize-sidebar btn btn-link btn-just-icon"
						onClick={this.handleMiniClick}
					>
						<i className="tim-icons icon-align-center visible-on-sidebar-regular text-muted" />
						<i className="tim-icons icon-bullet-list-67 visible-on-sidebar-mini text-muted" />
					</button>
				</div>
				<Sidebar
					{...this.props}
					routes={routes}
					activeColor={activeColor}
					logo={{
						outterLink: "/",
						text: "Hfam",
						imgSrc: logo
					}}
					closeSidebar={this.closeSidebar}
				/>
				<div
					className="main-panel"
					ref={this.mainPanel}
					data={activeColor}
				>
					<DefaultNavbar
						{...this.props}
						brandText={this.getActiveRoute(routes)}
						sidebarOpened={this.state.sidebarOpened}
						toggleSidebar={this.toggleSidebar}
					/>
					<Switch>
						{this.getRoutes(routes)}
						<Redirect from="*" to="/admin/dashboard" />
					</Switch>
					<Footer fluid />
				</div>
			</div>
		);
	}
}

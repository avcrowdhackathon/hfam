import React from "react";
import {NavItem, NavLink} from "reactstrap";

export function FooterLink({ href, description }) {
	return (
		<NavItem>
			<NavLink href={href}>{description}</NavLink>
		</NavItem>
	);
}

import React from "react";
import { Container, Nav } from "reactstrap";
import PropTypes from "prop-types";
import { FooterLink } from "./FooterLink";

export function Footer(props) {
	const footerClasses = "footer" + (props.default ? "footer-default" : "");
	return (
		<footer className={footerClasses}>
			<Container fluid={props.fluid}>
				<Nav>
					<FooterLink
						href="https://www.creative-tim.com"
						description="Creative Tim"
					/>
					<FooterLink
						href="https://www.creative-tim.com/presentation"
						description="About us"
					/>
					<FooterLink
					href="https://blog.creative-tim.com"
						description="Blog"
					/>
				</Nav>
				<div className="copyright">
					© {new Date().getFullYear()} made with{" "}
					<i className="tim-icons icon-heart-2" /> by{" "}
					<a
						href="https://www.creative-tim.com/"
						rel="noopener noreferrer"
						target="_blank"
					>
						Creative Tim
					</a>{" "}
					for a better web.
				</div>
			</Container>
		</footer>
	);
}

Footer.propTypes = {
	default: PropTypes.bool,
	fluid: PropTypes.bool
};

export default Footer;

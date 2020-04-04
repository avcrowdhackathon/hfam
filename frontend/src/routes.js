import Dashboard from "./components/Dashboard/Dashboard";
import ReactTables from "./views/tables/ReactTables.js";
import RegularTables from "./views/tables/RegularTables.js";
import ExtendedTables from "./views/tables/ExtendedTables.js";
import ValidationForms from "views/forms/ValidationForms.js";
import ExtendedForms from "views/forms/ExtendedForms.js";
import RegularForms from "views/forms/RegularForms.js";
import Widgets from "views/Widgets.js";
import Charts from "views/Charts.js";
import Buttons from "views/components/Buttons.js";
import SweetAlert from "views/components/SweetAlert.js";
import Notifications from "views/components/Notifications.js";
import Grid from "views/components/Grid.js";
import Typography from "views/components/Typography.js";
import Panels from "views/components/Panels.js";
import Timeline from "views/pages/Timeline.js";
import User from "views/pages/User.js";

import { HospitalDashboard } from "./components/Hospitals/HospitalsDashboard/HospitalsDashboard";
import { RegionDashboard } from "./components/RegionDashboard/RegionDashboard";
import { InputsForm } from "./components/InputsForm/InputsForm";

const routes = [
	{
		collapse: true,
		name: "Hfam",
		rtlName: "صفحات",
		icon: "tim-icons icon-image-02",
		state: "pagesCollapse",
		views: [
			{
				path: "/dashboard",
				name: "Dashboard",
				icon: "tim-icons icon-chart-pie-36",
				component: Dashboard,
				layout: "/admin",
			},
			{
				path: "/hospitals",
				name: "Hospitals",
				icon: "fas fa-map",
				component: HospitalDashboard,
				layout: "/admin",
			},
			{
				path: "/regions",
				name: "Region",
				icon: "fas fa-map",
				component: RegionDashboard,
				layout: "/admin",
			},
			{
				path: "/inputs",
				name: "Inputs",
				icon: "fas fa-edit",
				component: InputsForm,
				layout: "/admin",
			},
		],
	},
	{
		collapse: true,
		name: "Pages",
		rtlName: "صفحات",
		icon: "tim-icons icon-image-02",
		state: "pagesCollapse",
		views: [
			{
				path: "/timeline",
				name: "Timeline",
				rtlName: "تيالجدول الزمني",
				mini: "T",
				rtlMini: "تي",
				component: Timeline,
				layout: "/admin",
			},
			{
				path: "/user-profile",
				name: "User Profile",
				rtlName: "ملف تعريفي للمستخدم",
				mini: "UP",
				rtlMini: "شع",
				component: User,
				layout: "/admin",
			},
		],
	},
	{
		collapse: true,
		name: "Components",
		rtlName: "المكونات",
		icon: "tim-icons icon-molecule-40",
		state: "componentsCollapse",
		views: [
			{
				collapse: true,
				name: "Multi Level Collapse",
				rtlName: "انهيار متعدد المستويات",
				mini: "MLT",
				rtlMini: "ر",
				state: "multiCollapse",
				views: [
					{
						path: "/buttons",
						name: "Buttons",
						rtlName: "وصفت",
						mini: "B",
						rtlMini: "ب",
						component: Buttons,
						layout: "/admin",
					},
				],
			},
			{
				path: "/buttons",
				name: "Buttons",
				rtlName: "وصفت",
				mini: "B",
				rtlMini: "ب",
				component: Buttons,
				layout: "/admin",
			},
			{
				path: "/grid-system",
				name: "Grid System",
				rtlName: "نظام الشبكة",
				mini: "GS",
				rtlMini: "زو",
				component: Grid,
				layout: "/admin",
			},
			{
				path: "/panels",
				name: "Panels",
				rtlName: "لوحات",
				mini: "P",
				rtlMini: "ع",
				component: Panels,
				layout: "/admin",
			},
			{
				path: "/sweet-alert",
				name: "Sweet Alert",
				rtlName: "الحلو تنبيه",
				mini: "SA",
				rtlMini: "ومن",
				component: SweetAlert,
				layout: "/admin",
			},
			{
				path: "/notifications",
				name: "Notifications",
				rtlName: "إخطارات",
				mini: "N",
				rtlMini: "ن",
				component: Notifications,
				layout: "/admin",
			},
			{
				path: "/typography",
				name: "Typography",
				rtlName: "طباعة",
				mini: "T",
				rtlMini: "ر",
				component: Typography,
				layout: "/admin",
			},
		],
	},
	{
		collapse: true,
		name: "Forms",
		rtlName: "إستمارات",
		icon: "tim-icons icon-notes",
		state: "formsCollapse",
		views: [
			{
				path: "/regular-forms",
				name: "Regular Forms",
				rtlName: "أشكال عادية",
				mini: "RF",
				rtlMini: "صو",
				component: RegularForms,
				layout: "/admin",
			},
			{
				path: "/extended-forms",
				name: "Extended Forms",
				rtlName: "نماذج موسعة",
				mini: "EF",
				rtlMini: "هوو",
				component: ExtendedForms,
				layout: "/admin",
			},
			{
				path: "/validation-forms",
				name: "Validation Forms",
				rtlName: "نماذج التحقق من الصحة",
				mini: "VF",
				rtlMini: "تو",
				component: ValidationForms,
				layout: "/admin",
			},
		],
	},
	{
		collapse: true,
		name: "Tables",
		rtlName: "الجداول",
		icon: "tim-icons icon-puzzle-10",
		state: "tablesCollapse",
		views: [
			{
				path: "/regular-tables",
				name: "Regular Tables",
				rtlName: "طاولات عادية",
				mini: "RT",
				rtlMini: "صر",
				component: RegularTables,
				layout: "/admin",
			},
			{
				path: "/extended-tables",
				name: "Extended Tables",
				rtlName: "جداول ممتدة",
				mini: "ET",
				rtlMini: "هور",
				component: ExtendedTables,
				layout: "/admin",
			},
			{
				path: "/react-tables",
				name: "React Tables",
				rtlName: "رد فعل الطاولة",
				mini: "RT",
				rtlMini: "در",
				component: ReactTables,
				layout: "/admin",
			},
		],
	},
	{
		path: "/widgets",
		name: "Widgets",
		rtlName: "الحاجيات",
		icon: "tim-icons icon-settings",
		component: Widgets,
		layout: "/admin",
	},
	{
		path: "/charts",
		name: "Charts",
		rtlName: "الرسوم البيانية",
		icon: "tim-icons icon-chart-bar-32",
		component: Charts,
		layout: "/admin",
	},
];

export default routes;

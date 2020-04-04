import { useState } from "react";

const useForm = (callback, initialState = {}) => {
	const [values, setValues] = useState(initialState);

	const handleSubmit = (event) => {
		if (event) {
			event.preventDefault();
			callback();
		}
	};

	const handleChange = (event) => {
		event.persist();
		if (event.target.type === "range") {
			setValues((values) => ({
				...values,
				[event.target.name]: event.target.value / 100,
			}));
		} else if (event.target.type === "date") {
			function formatDate(date) {
				var d = new Date(date),
					month = "" + (d.getMonth() + 1),
					day = "" + d.getDate(),
					year = d.getFullYear();

				if (month.length < 2) month = Number(month);
				if (day.length < 2) day = Number(day);

				return [year, month, day].join("-");
			}
			setValues((values) => ({
				...values,
				[event.target.name]: formatDate(event.target.value),
			}));
		} else if(event.target.type === "number") {
			setValues((values) => ({
				...values,
				[event.target.name]: Number(event.target.value),
			}));
		} else {
			setValues((values) => ({
				...values,
				[event.target.name]: event.target.value,
			}));
		}
	};

	return {
		handleChange,
		handleSubmit,
		values,
	};
};

export { useForm };

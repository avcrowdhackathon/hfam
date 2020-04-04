import {useState, useEffect} from "react";

export function useApi(url) {
    const [isLoading, setLoading] = useState(true);
    const [data, setData] = useState(null);

    useEffect(() => {
        fetch(url)
            .then(res => res.json())
            .then(json => {
                setLoading(false);
                setData(json);
            })
            .catch(err => console.log(err));
    })

    return [isLoading, data];
}
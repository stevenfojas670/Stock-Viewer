"use client"
import React, { useEffect, useState } from "react"

export default function Home() {
	const [message, setMessage] = useState("...") //Could set use state to an animation while the data is being fetched
	const [people, setPeople] = useState([])

	useEffect(() => {
		fetch("http://localhost:8080/home") //Is there a way to have better linked endpoints?
			.then((response) => response.json())
			.then((data) => {
				setMessage(data.message)
				setPeople(data.people)
			})
	}, [])

	return (
		<main>
			<div>
				<h1>{message}</h1>
			</div>
			<div>
				{people.map((person, index) => (
					<div key={index}>{person}</div>
				))}
			</div>
		</main>
	)
}

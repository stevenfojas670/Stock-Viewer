"use client"
import React, { useEffect, useState } from "react"
import { Container, Grid, Button, Card, CardContent, Typography, CardActions } from '@mui/material'

export default function Home() {
	const [prices, setPrices] = useState([]) //Could set use state to an animation while the data is being fetched

	useEffect(() => {
		fetch("http://localhost:8080/") //Is there a way to have better linked endpoints?
			.then((response) => response.json())
			.then((data) => {
				setPrices(data)
				console.log(data)
			})
	}, [])

	return (
		<main>
			<Container sx={{ justifyContent: 'center', alignItems: 'center'}}>
				<Grid container spacing={2}>
					{prices.map((data, id) => (
						<Grid item key={id}>
							<Card>
								<CardContent>
									<Typography>{data.symbol}</Typography>
									<Typography>Initial Price: {data.initial_price}</Typography>
								</CardContent>
								<CardActions>
									<Button size="small">Details</Button>
								</CardActions>
							</Card>
						</Grid>
					))}
				</Grid>
			</Container>
		</main>
	)
}

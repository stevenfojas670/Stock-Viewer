"use client";
import {
  createTheme,
  replace,
  responsiveFontSizes,
} from "@mui/material/styles";
import { Inter } from "next/font/google";

const inter = Inter({ subsets: ["latin"] });

const theme = createTheme({});

export default responsiveFontSizes(theme);

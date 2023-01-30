import express from "express";
import mongoose from "mongoose";
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const app = express();
const router = express.Router();
const PORT = process.env.PORT || 3000;

app.use(express.static(path.join(__dirname, "..", "build")));
app.use(express.json());

//connecting to mongoDB
const username = "";
const password = "";
const cluster = "";

mongoose.connect(
	`mongodb+srv://${username}:${password}@${cluster}.mongodb.net/?retryWrites=true&w=majority`,
	{
		useNewUrlParser: true,
		useUnifiedTopology: true,
	}
);
const db = mongoose.connection;
db.on("error", console.error.bind(console, "connection error: "));
db.once("open", function () {
	console.log("Connected successfully");
});

app.use("/api", router);

app.get("*", async (req, res) => {
	res.sendFile(path.join(__dirname, "..", "build", "index.html"));
});

app.listen(PORT, () => console.log(`Server listening on port ${PORT}`));

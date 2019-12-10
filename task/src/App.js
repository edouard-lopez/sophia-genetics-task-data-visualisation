import * as d3 from "d3";
import { DateTime } from "luxon";
import React from "react";
import "./assets/App.css";
import { data, domainX } from "./assets/data";
import UserUsageGraph from "./UserUsageGraph";

const dateRange = (start, end) =>
  d3
    .scaleTime()
    .domain([start, end])
    .ticks()
    .map(value => DateTime.fromISO(value.toISOString()).toFormat("MM-yyyy"));

const prepare = (range, data) =>
  range.map((date, index) => {
    return {
      x: date,
      actual: data.actualUsage[index],
      predicted: data.predictedUsage[index]
    };
  });

function App() {
  const userData = data[0];
  const from = DateTime.fromFormat(domainX.from, "MM-yyyy");
  const to = DateTime.fromFormat(domainX.to, "MM-yyyy");

  return (
    <div className="App">
      <div className="App-header">
        <div className="container">
          <UserUsageGraph data={prepare(dateRange(from, to), userData)} />
        </div>
      </div>
    </div>
  );
}

export default App;

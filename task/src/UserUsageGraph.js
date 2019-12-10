import {
  Legend,
  LineChart,
  Line,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip
} from "recharts";

import React, { Component } from "react";

class DataViz extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    const { data } = this.props;

    return (
      <LineChart
        width={600}
        height={300}
        data={data}
        margin={{ top: 5, right: 20, bottom: 5, left: 0 }}
      >
        <Line type="monotone" dataKey="actual" stroke="#8884d8" />
        <Line type="monotone" dataKey="predicted" stroke="#82ca9d" />
        <CartesianGrid stroke="#ccc" strokeDasharray="5 5" />
        <XAxis dataKey="x" />
        <YAxis />
        <Tooltip />
        <Legend />
      </LineChart>
    );
  }
}

export default DataViz;

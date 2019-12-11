import * as d3 from "d3";
import { DateTime } from "luxon";
import React, { Component } from "react";
import "./assets/App.css";
import UserUsageGraph from "./UserUsageGraph";
import axios from "axios";

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

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isLoading: false,
      domainX: {},
      userData: []
    };
  }

  async componentDidMount() {
    this.setState({ isLoading: true });
    try {
      const response = await axios.get("http://localhost/domain-x");
      this.setState({ domainX: response.data, isLoading: false });
    } catch (error) {
      this.setState({ error, isLoading: false });
    }
    try {
      const response = await axios.get("http://localhost/user-usage");
      this.setState({ userData: response.data, isLoading: false });
    } catch (error) {
      this.setState({ error, isLoading: false });
    }
  }

  render() {
    const { domainX, userData, isLoading } = this.state;
    if (userData.length < 1) {
      return <h1>Loading ...</h1>;
    }

    const from = DateTime.fromFormat(domainX.from, "MM-yyyy");
    const to = DateTime.fromFormat(domainX.to, "MM-yyyy");

    return (
      <div className="App">
        <div className="App-header">
          <div className="container">
            <UserUsageGraph data={prepare(dateRange(from, to), userData[0])} />
          </div>
        </div>
      </div>
    );
  }
}

export default App;

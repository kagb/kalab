import React from 'react';
import ReactDOM from 'react-dom';

var ATag = React.createClass({
  render: function(){
    return (<a className="a-tag">{this.props.tag_name}</a>)
  }
});

var PTag = React.createClass({
  render: function(){
    return (<p className="p-tag">{this.props.text}</p>)
  }
}); 

var Main = React.createClass({
  getInitialState: function(){
    return {date: new Date()};
  },

  set_time: function(){
    window.setTimeout(function() {
        this.setState({date: new Date()})
    }.bind(this), 1000);
  },

  componentDidMount: function(){
    this.set_time();
  },

  componentDidUpdate: function(){
    this.set_time();
  },

  render: function(){
    return (
      <div className="main">
        <PTag text="Hi, this is Ka'Lab." />
        <PTag text={"It's " + this.state.date.toString()} />
        <PTag text="2311 guys had visited this page, much thanks." />
      </div>
    );
  }
});

ReactDOM.render(
    <Main />,
    document.getElementById('kalab')
);

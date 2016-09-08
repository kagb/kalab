import React from 'react';
import ReactDOM from 'react-dom';
import $ from 'jquery'; 

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
    this.serverRequest = $.get('/api/pv?page=index', function(data){
      this.setState({pv: data.pv});
    }.bind(this));
  },

  componentDidUpdate: function(){
    this.set_time();
  },

  render: function(){
    return (
      <div className="main">
        <PTag text="Hi, this is Ka'Lab." />
        <PTag text={"It's " + this.state.date.toString()} />
        <PTag text={this.state.pv + " guys have visited this page, much thanks."} />
      </div>
    );
  }
});

ReactDOM.render(
    <Main />,
    document.getElementById('kalab')
);

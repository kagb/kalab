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
  render: function(){
    return (
      <div className="main">
        <PTag text="Hi, this is Ka'Lab." />
        <PTag text="It’s Friday Aug. 12, 2016, the 225 day of 2016." />
        <PTag text="2311 guys had visited this page, much thanks." />
      </div>
    );
  }
});

ReactDOM.render(
    <Main />,
    document.getElementById('kalab')
);

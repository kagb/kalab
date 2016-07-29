import React from 'react';
import ReactDOM from 'react-dom';

var CenterText = React.createClass({
  render: function(){
    return (<div class="center-txt"> {this.props.txt} </div>);
  }
});

ReactDOM.render(<CenterText txt="Hi, this is Ka'Lab" />, document.getElementById('kalab'));

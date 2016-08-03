import React from 'react';
import ReactDOM from 'react-dom';

var i_names = ['ABOUT', 'BLOG', 'TODAY', 'NLP-T', 'GOLANG', 'SPIDER'];

var IndexTag = React.createClass({
  render: function(){
    return (<li className="i-tag">{this.props.tag_name}</li>)
  }
});

var Tags = React.createClass({
  render: function(){
    return (
    <div className="tags">
      <ui>
        {
          i_names.map(function (name){
            return <IndexTag tag_name={name} />
          })
        }
      </ui>
    </div>
    )
  }
});

var Main = React.createClass({
  render: function(){
    return (
      <div className="page">
        <div className="m-txt"> {this.props.txt} </div>
        <Tags />
      </div>
    );
  }
});

ReactDOM.render(<Main txt="Hi, this is Ka'Lab" />, document.getElementById('kalab'));

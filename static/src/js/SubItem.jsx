import React from 'react';

class SubItem extends React.Component {
   render() {
         return (
             <div class='sub-item'>
                <a href={this.props.go_to}>
                  {this.props.txt}
                </a>
             </div>
         );
      }
}

export default SubItem;

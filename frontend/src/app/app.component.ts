import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Angular Quiz';
  const convertFile = () => {
  const input = document.getElementById('fileInput');

  const reader = new FileReader();
  reader.onload = () => {
    let text = reader.result;
    console.log('CSV: ', text.substring(0, 100) + '...');

    //convert text to json here
    //var json = this.csvJSON(text);
  };
  reader.readAsText(input.files[0]);
};
}

import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-sm-device-icon',
  standalone: true,
  imports: [],
  templateUrl: './sm-device-icon.component.html',
  styleUrl: './sm-device-icon.component.scss'
})
export class SmDeviceIconComponent {
  @Input("icon") iconName = '';
}

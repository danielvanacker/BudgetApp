import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'info-card',
  templateUrl: './info-card.component.html',
  styleUrls: ['./info-card.component.scss']
})
export class InfoCardComponent implements OnInit {
  @Input() icon: any;
  @Input() category: string;
  @Input() value: string;
  @Input() colorClass: string;

  constructor() {}

  ngOnInit(): void {
  }

}

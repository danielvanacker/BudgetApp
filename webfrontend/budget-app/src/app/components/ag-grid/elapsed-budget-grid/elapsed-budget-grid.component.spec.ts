import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ElapsedBudgetGridComponent } from './elapsed-budget-grid.component';

describe('ElapsedBudgetGridComponent', () => {
  let component: ElapsedBudgetGridComponent;
  let fixture: ComponentFixture<ElapsedBudgetGridComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ElapsedBudgetGridComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ElapsedBudgetGridComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

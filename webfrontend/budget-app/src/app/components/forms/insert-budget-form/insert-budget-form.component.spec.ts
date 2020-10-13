import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { InsertBudgetFormComponent } from './insert-budget-form.component';

describe('InsertBudgetFormComponent', () => {
  let component: InsertBudgetFormComponent;
  let fixture: ComponentFixture<InsertBudgetFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ InsertBudgetFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(InsertBudgetFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

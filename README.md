# Solving integer linear Programming
* Please see problem statement here: [problem.pdf](https://github.com/Harshit0143/Integer_Linear_Porgramming/blob/main/problem.pdf)


# Saddle Point: minimum in row, maximum in column. 
<img width="1147" alt="Screenshot 2023-04-28 at 5 57 26 PM" src="https://user-images.githubusercontent.com/97736991/235147168-4e219aa6-d677-4dac-a73d-e8a82dcea9ef.png">


<img width="740" alt="Screenshot 2023-04-30 at 11 16 26 AM" src="https://user-images.githubusercontent.com/97736991/235337757-354a8bac-7d73-4850-9880-925eb1f9aa46.png">

<img width="1493" alt="Screenshot 2023-04-30 at 12 37 53 PM" src="https://user-images.githubusercontent.com/97736991/235340500-ca7497c3-152d-4b33-8663-d3e31920faed.png">
<img width="1436" alt="Screenshot 2023-04-30 at 12 49 14 PM" src="https://user-images.githubusercontent.com/97736991/235340906-5e031d0c-06b8-427e-876f-a27b3e4c36bc.png">
<img width="1361" alt="Screenshot 2023-04-30 at 1 12 33 PM" src="https://user-images.githubusercontent.com/97736991/235341723-e9d615af-4c26-47b7-a8f1-c67e90ae46ff.png">
<img width="1401" alt="Screenshot 2023-04-30 at 1 13 10 PM" src="https://user-images.githubusercontent.com/97736991/235341750-d565505a-853d-40ea-8396-4a46cc673d41.png">

<img width="782" alt="Screenshot 2023-04-30 at 1 57 11 PM" src="https://user-images.githubusercontent.com/97736991/235343419-fc779763-4633-4e4e-9543-47a10494a6c8.png">
<img width="1160" alt="Screenshot 2023-04-30 at 2 04 03 PM" src="https://user-images.githubusercontent.com/97736991/235343660-d3ae4a92-b90d-46e8-a872-cb55f25f13d0.png">
<img width="1023" alt="Screenshot 2023-04-30 at 2 08 55 PM" src="https://user-images.githubusercontent.com/97736991/235343884-f88fd356-46fc-4334-8ab7-6c4df371360d.png">
<img width="501" alt="Screenshot 2023-04-30 at 2 19 11 PM" src="https://user-images.githubusercontent.com/97736991/235344284-4635e201-4426-44cc-8b60-ee8755ee3a81.png">
<img width="561" alt="Screenshot 2023-04-30 at 2 25 20 PM" src="https://user-images.githubusercontent.com/97736991/235344548-ff608f64-d43d-4c46-8d8e-79536bac8594.png">

* the u_i >= 0 and v_j >= 0 for each i and j because we want to penalise for breaking `any` constraint and NOT `atleast one` 

<img width="749" alt="Screenshot 2023-04-30 at 2 26 55 PM" src="https://user-images.githubusercontent.com/97736991/235344614-5693bf80-5b41-43f8-bed3-f6d6b1d24ec0.png">

<img width="902" alt="Screenshot 2023-05-01 at 4 24 20 PM" src="https://user-images.githubusercontent.com/97736991/235443037-1341f0e5-e3d4-450c-911a-ff0aa2c19066.png">

<img width="871" alt="Screenshot 2023-05-01 at 4 24 35 PM" src="https://user-images.githubusercontent.com/97736991/235443055-94483d06-b7d3-4b94-ac4c-1894162a1f87.png">

<br>
# Problem Notes 
<img width="1393" alt="Screenshot 2023-05-01 at 9 21 55 PM" src="https://user-images.githubusercontent.com/97736991/235481877-d02b8202-6de2-472e-a0fa-dc1c2b536914.png">
<img width="743" alt="Screenshot 2023-05-01 at 9 32 29 PM" src="https://user-images.githubusercontent.com/97736991/235483623-b05f2fda-5359-4181-9dae-713bbd4ba2db.png">


<img width="780" alt="Screenshot 2023-05-01 at 9 32 41 PM" src="https://user-images.githubusercontent.com/97736991/235483647-9f8a1779-c011-452d-90d3-0809bf968c56.png">
<img width="745" alt="Screenshot 2023-05-01 at 9 44 46 PM" src="https://user-images.githubusercontent.com/97736991/235485613-05566531-12c7-466e-abac-7e69d06e5154.png">
<img width="687" alt="Screenshot 2023-05-01 at 10 04 10 PM" src="https://user-images.githubusercontent.com/97736991/235488706-ec3a8833-36f0-4ce1-b42e-17fd4f972e08.png">

<img width="1241" alt="Screenshot 2023-05-02 at 1 05 19 AM" src="https://user-images.githubusercontent.com/97736991/235517036-fe67841c-e60c-4f81-b2cb-6bb19f17e2c4.png">


<img width="804" alt="Screenshot 2023-05-02 at 11 33 46 AM" src="https://user-images.githubusercontent.com/97736991/235590939-a0340e10-b05d-4ee6-8aa0-f2a0c1462c7f.png">






<img width="1027" alt="Screenshot 2023-05-02 at 1 42 32 PM" src="https://user-images.githubusercontent.com/97736991/235614207-cddf9083-4214-4c70-8355-3ff9fca84a62.png">


let $c_1..........c_N$ and $d_1..........d_N$ represent:        
$s$: virtual node:
$c_i$: Clean cloths availabe on $i^{th}$ day.      
$d_i$: dirty cloths on $i^{th}$ day.  
Edges:           
* $c_i to d_i$ of $lb = r_i$ and $ub = r_i$. We don't need an upper bound actually. We can give an exchange argument for this that optimal solution will always have flow in the edge = $lb(e)$
* for each $i = 1,2....N$ $s \to c_i$  with $lb = p$
* $d_i \to $  
You are looking for the minimum feasible flow. 












